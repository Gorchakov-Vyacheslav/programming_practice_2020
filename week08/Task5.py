def filling_matrix(x):
    if np.isnan(x).all():
        y = np.nan_to_num(x, nan=0)
    else:
        y = np.nan_to_num(x, nan=x.mean())
    return y
print(filling_matrix(x))