import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

class App :
    #### PUBLIC ####

    def __init__(self, title=None, ylabel=None, xlabel=None) -> None:
        """
            Initializes the application space
        """

        # Set class variables
        self.__title=title
        self.__xlabel=xlabel
        self.__ylabel=ylabel

        pass

    def enter(self) ->None :
        """
            Main application functionality
        """

        # Create the Plot
        fig, ax = plt.subplots()
        plt.title(self.__title)
        plt.xlabel(self.__xlabel)
        plt.ylabel(self.__ylabel)
    
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

    #### PRIVATE ####

    __title = None
    __xlabel = None
    __ylabel = None

    pass

if __name__ == "__main__" :
    """
        Primary software application entry point
    """

    # Initialization
    xlabel = "Possible Ratings"
    ylabel = "Prof Ratings"
    title = "Shitty profs ratings"
    app = App(xlabel=xlabel, ylabel=ylabel, title=title)
    
    # Software Logic
    app.enter()

    pass
