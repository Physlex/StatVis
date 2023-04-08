import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # Create the Plot
    fig, ax = plt.subplots()
    plt.ylabel("Prof Ratings")
    plt.xlabel("Possible Ratings")
    plt.title("Shitty profs ratings")

    # Create the Axes for the Plot
    ratings = [1, 2, 3, 4, 5]
    num_ratings = [22, 39, 37, 51, 67]

    ax.bar(height=num_ratings, x=ratings)

    # Determine the number of samples
    num_samples = int(0)

    for i in range(len(num_ratings)) :
        num_samples += num_ratings[i]

    # Determine the sample mean
    sample_mean = 0

    sum = int(0)
    for i in range(len(ratings)) :
        sum += ratings[i] * num_ratings[i]

    if (num_samples > 0) :
        sample_mean = sum / num_samples

    # Determine the sample variance
    sample_variance = 0
 
    dist_from_mean = 0
    for i in range(len(ratings)) :
        sample_variance = ( (ratings[i] - sample_mean) ** 2 ) * num_ratings[i]

    if (sample_variance != 0) :
        sample_variance /= (num_samples - 1)

    # Display all Data
    print(f"sample mean: {sample_mean}, sample variance: {sample_variance}, SD: {np.sqrt(sample_variance)}")
    plt.show()

    pass
