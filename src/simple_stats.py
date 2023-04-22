class SimpleStats :
    """
        Defines \'Simple\' math constructs used frequently in statistics
    """

    #### PUBLIC ####

    def __init__(self) -> None:
        """
            Creates SimpleMath Object
        """

        pass

    def num_samples(self, y_data_stream :list) -> int :
        """
            Determine the number of instances of an x_data_stream random variable
        """

        num_samples = int(0)
        for i in range(len(y_data_stream)) :
            num_samples += y_data_stream[i]

        return num_samples

    def sample_mean(self, x_data_stream :list, y_data_stream :list, num_samples :int) -> float :
        """
            Construct the sample mean from the x and y streams, adjusts the x stream by number of instances
            defined as y.
        """

        # HEADER GUARD
        if (len(x_data_stream) != len(y_data_stream)) :
            print("Error: data stream input has non zero difference in length")
            return None

        # Construct \${Y\bar}
        sum = int(0)
        for i in range(len(x_data_stream)) :
            sum += x_data_stream[i] * y_data_stream[i]

        # Divide out the mean
        sample_mean = float(0)
        if (num_samples > 0) :
            sample_mean = float(sum / num_samples)

        return sample_mean

    def sample_var(self, x_data_stream :list, y_data_stream :list, num_samples :int, sample_mean :float) -> float :
        """
            Calculate the sample variance when the population mean is unknown
        """

        # HEADER GUARD
        if (len(x_data_stream) != len(y_data_stream)) :
            print("Error: data stream input has non zero difference in length")
            return None
        elif (num_samples - 1 == 0) :
            print("Error: num_samples must be greater than 1")
            return None

        # Calculate the second raw moment about the sample mean
        sample_variance = float(0)
        for i in range(len(x_data_stream)) :
            sample_variance = ( (x_data_stream[i] - sample_mean) ** 2) * y_data_stream[i]

        # Determine sample variance
        sample_variance = sample_variance / (num_samples - 1)

        return sample_variance

    pass
