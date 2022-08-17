from glob import glob
import os

save_path = "rsi_divergence/README.md"
charts_dir = "rsi_divergence/charts"

with open(save_path, "w+") as f:
    for plot_path in glob(f"{charts_dir}/*.png"):
        img_src = plot_path.split("rsi_divergence/")[-1]
        line = f"<img src='{img_src}' width='800' height='400'>"
        f.write(line + "\n\n")
        print(f"Finished writing {plot_path}.")