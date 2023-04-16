# External
import matplotlib.pyplot as plt
import numpy as np

# Internal
from simple_stats import SimpleStats
from file import File

class App :
    """
        Abstraction for application logic.
        Controls rendering, 
    """
    #### PUBLIC ####

    def __init__(self) -> None:
        """
            Initializes the application space with class variables
        """
        pass

    def run(self, relative_file_path :str) -> None :
        """
            Main application functionality
        """
        # Read data streams from data file and assign labels
        x_label = str(None)
        x_data_stream = list()

        y_label = str(None)
        y_data_stream = list()

        # Clean Data
        bar_data_file = File(relative_file_path)
        file_lines = bar_data_file.read_contents()
        for i, line in enumerate(file_lines) :
            # Scan for the comma of this line
            comma_index = -1
            for j, char in enumerate(line) :
                if (char == ',') :
                    comma_index = j

            # Slice around comma and convert to relevant data types
            if (i == 0) :
                x_label = line[0 : comma_index]
                y_label = line[comma_index + 1 : len(line)]
            else :
                x_data_stream.append(int(line[0 : comma_index]))
                y_data_stream.append(int(line[comma_index + 1 : len(line)]))

        # Create the Plot
        fig, ax = plt.subplots()

        title = str("Shitty Professor's Ratings")
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        ax.bar(x_data_stream, y_data_stream)

        # Determine sample statistics
        stats = SimpleStats()
        num_samples = stats.num_samples(y_data_stream)
        sample_mean = stats.sample_mean(x_data_stream, y_data_stream, num_samples)
        sample_variance = stats.sample_var(x_data_stream, y_data_stream, num_samples, sample_mean)

        # Display Data
        print("sample mean: {:.2f}".format(sample_mean))
        print("sample variance: {:.2f}".format(sample_variance))
        print("sample deviation: {:.2f}".format(np.sqrt(sample_variance)))
        plt.show()

        pass

    pass
