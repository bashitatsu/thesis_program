import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

refseq = [330, 352, 353, 363, 377, 379, 380, 381, 395, 420, 422, 423, 435, 437, 438, 481, 487, 488, 495, 520]
alpha = [347, 348, 358, 372, 374, 375, 376, 390, 415, 417, 418, 430, 432, 433, 476, 482, 483, 484, 490, 495, 498]
beta = [347, 348, 358, 372, 374, 375, 376, 390, 415, 417, 418, 430, 432, 433, 476, 481, 482, 483, 490, 495, 498]
gamma = [350, 351, 361, 375, 377, 378, 379, 393, 418, 420, 421, 433, 435, 436, 479, 484, 485, 486, 493, 498, 501]
delta = [348, 349, 359, 373, 375, 376, 377, 391, 416, 418, 419, 431, 433, 434, 447, 476, 477, 483, 484, 491]
omicron = [334, 347, 348, 358, 371, 374, 375, 376, 390, 415, 417, 418, 430, 432, 470, 474, 475, 476, 482, 483, 494, 499]

l = [refseq,alpha,beta,gamma,delta,omicron]
l2 = []
for row in l:
    l2.append(pd.Series(row))

label = ["RefSeq","Alpha","Beta","Gamma","Delta","Omicron"]

df = pd.DataFrame()
for i in range(len(l2)):
    df[label[i]] = l2[i]

sns.stripplot(data = df,jitter=False,size=4)
plt.ylabel("Amino Acid(Number)", fontsize = 14)
plt.show()
