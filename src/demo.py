# This is a demo script for learning Streamlit
# I copied a simple demo from Seaborn to have something to display

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

def demo():
	# "Scatterplot with multiple semantics"
	# Link: https://seaborn.pydata.org/examples/different_scatter_variables.html

	sns.set_theme(style='whitegrid')

	# Load the example diamonds dataset
	diamonds = sns.load_dataset("diamonds")

	# Draw a scatter plot while assigning point colors and sizes to different variables in the dataset
	fig, ax = plt.subplots(figsize=(6.5, 6.5))

	sns.despine(fig, left=True, bottom=True)
	clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
	sns.scatterplot(x="carat", y="price",
		hue='clarity', size='depth',
		palette='ch:r=-.2,d=.3_r',  # no idea what this means
		hue_order=clarity_ranking,
		sizes=(1, 8), linewidth=0,
		data=diamonds, ax=ax
		)

	plt.suptitle("Demo: Scatterplot with multiple semantics", 
					x=0.05, ha='left', fontsize='x-large', fontweight='bold')
	ax.set_title("The impact of clarity, depth, and carat on the price of diamonds.",
					x=0, ha='left')

	# fig.savefig("demo_plot.png")
	# plt.show()
	return fig

if __name__ == "__main__":
	f = demo()
	plt.show()
	plt.close(f)
