import numpy as np
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

a = np.array([172,174,176,172,172,173,176,172,177,174,176,175,176,169,175,174,174,174,175,173,171,171,175,175,173,175,175])

print(np.mean(a))
print(np.median(a))
print(stats.mode(a))

b = np.array([184,180,181,184,182,181,182,182,183,182,181,182,182,180,183,181,184,183,182,182,183,182,183,181,180,181,183])

print(np.std(b))


a.sort()
hmean = np.mean(a)
hstd = np.std(a)
pdf = stats.norm.pdf(a, hmean, hstd)
plt.plot(a, pdf) # including h here is crucial
plt.show()
