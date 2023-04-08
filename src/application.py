# External
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Internal
from simple_stats import SimpleStats

class App :
    #### PUBLIC ####

    def __init__(self) -> None:
        """
            Initializes the application space with class variables
        """

        pass

    def run(self) ->None :
        """
            Main application functionality
        """

        # Create the Plot
        title = str("Shitty Professor's Ratings")
        x_label = str("Rating Categories")
        y_label = str("Number of Ratings")

        fig, ax = plt.subplots()
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        # Create the Axes for the Plot
        ratings = [1, 2, 3, 4, 5]
        num_ratings = [22, 39, 37, 51, 67]

        ax.bar(ratings, num_ratings)

        # Determine sample statistics
        stats = SimpleStats()
        num_samples = stats.num_samples(num_ratings)
        sample_mean = stats.sample_mean(ratings, num_ratings, num_samples)
        sample_variance = stats.sample_var(ratings, num_ratings, num_samples, sample_mean)

        # Display Data
        print(f"sample mean: {sample_mean}\n"
              f"sample variance: {sample_variance}\n"
              f"sample deviation: {np.sqrt(sample_variance)}"
        )
        plt.show()

        pass

    pass
