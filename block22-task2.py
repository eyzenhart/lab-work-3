def partial_sums(*args, p_sum=[0], ind=0):
    if ind < len(args):
        sum = p_sum[-1]
        sum += args[ind]
        p_sum.append(sum)
        ind += 1
        partial_sums(*args, p_sum=p_sum, ind=ind)
    else:
        print(p_sum)


partial_sums(1, 0.5, 0.25, 0.125)

