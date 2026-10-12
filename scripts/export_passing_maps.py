"""Export four player passing maps for Chelsea vs Arsenal (19 Sep 2015).

Data: StatsBomb Open Data. The plots reproduce the Phase 1 notebook's
passing-map method and are intended for the GitHub portfolio gallery.

Run: python scripts/export_passing_maps.py
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
from mplsoccer import Pitch
from statsbombpy import sb

MATCH_ID = 3754217
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "visualizations" / "passing-maps"

PLAYERS = {
    "Francesc Fàbregas i Soler": "fabregas_pass_map.png",
    "Mesut Özil": "ozil_pass_map.png",
    "Theo Walcott": "walcott_pass_map.png",
    "Santiago Cazorla González": "cazorla_pass_map.png",
}


def main():
    events = sb.events(match_id=MATCH_ID)
    passes = events.loc[events["type"] == "Pass"].copy()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for player_name, filename in PLAYERS.items():
        player_passes = passes.loc[passes["player"] == player_name].copy()
        if player_passes.empty:
            raise ValueError(f"No passes found for {player_name!r}; check event data.")

        completed = player_passes.loc[player_passes["pass_outcome"].isna()]
        other_outcomes = player_passes.loc[player_passes["pass_outcome"].notna()]

        pitch = Pitch(
            pitch_type="statsbomb",
            pitch_color="grass",
            line_color="white",
            stripe=True,
        )
        fig, ax = pitch.draw(figsize=(14, 9))

        def add_arrows(frame, color, label):
            if frame.empty:
                return
            starts = pd.DataFrame(frame["location"].tolist(), index=frame.index)
            ends = pd.DataFrame(frame["pass_end_location"].tolist(), index=frame.index)
            pitch.arrows(
                starts.iloc[:, 0], starts.iloc[:, 1],
                ends.iloc[:, 0], ends.iloc[:, 1],
                ax=ax, color=color, width=1.5, headwidth=4,
                headlength=5, alpha=0.7, label=label,
            )

        add_arrows(completed, "#7ee081", "Completed")
        add_arrows(other_outcomes, "#ff7474", "Other outcomes")

        ax.legend(loc="upper left")
        ax.set_title(
            f"{player_name} | Chelsea vs Arsenal 2015/16",
            fontsize=15, pad=15,
        )

        output_path = OUTPUT_DIR / filename
        fig.savefig(output_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"{output_path.name}: {len(player_passes)} passes "
              f"({len(completed)} completed, {len(other_outcomes)} other)")


if __name__ == "__main__":
    main()
