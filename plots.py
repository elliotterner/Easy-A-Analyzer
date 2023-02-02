import matplotlib.pyplot as plt

# ggplot, seaborn-v0_8-notebook, _classic_test_patch
plt.style.use('seaborn')
fig, axs  = plt.subplots(1, 2)         # create subplot with 1 row, 2 cols
font = {'family': 'sans-serif', 'size': 16, 'weight': 'bold'}
bar_width = 0.6


# Data for Graph 1
graph_one_x = ["J. Stenvek", "A. Hornof", "E. Wills", "M. Young"]
a_prec = [64.2, 62.2, 70, 32]
axs[0].bar(graph_one_x, a_prec, bar_width)
axs[0].set_ylim(0, 100)
axs[0].set_ylabel("% As")
axs[0].set_xlabel("Instructors")
axs[0].set_title("CS Dept", fontdict=font)
axs[0].grid(True)
axs[0].xaxis.grid(False)


#Data for Graph 2
graph_two_x= ["J. Stenvek", "A. Hornof", "E. Wills", "M. Young"]
df_prec = [14.2, 12.2, 5, 11]
axs[1].bar(graph_two_x, df_prec, bar_width)
axs[1].set_ylim(0, 100)
axs[1].set_ylabel("% Ds and Fs")
axs[1].set_xlabel("Instructors")
axs[1].set_title("CS Dept", fontdict=font)
axs[1].grid(True)
axs[1].xaxis.grid(False)

# Graph Output
plt.tight_layout()
plt.show()


#plt.savefig("results.png") saves as png to directory