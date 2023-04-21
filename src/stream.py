# INTERNAL
from file import File

class Stream :
    """
        Stream accepts a file name and returns
        a 'stream' (a list) of data and it's associated
        label.

        Stream acts differently depending on the type of
        data input. For example:

        - CSV files are read and returned w/ a label and list of
          associated pairs.

        - TXT files are read 'raw' i.e. they directly return a list
          of words indexed by line.
    """
    #### PUBLIC ####

    #### INTERFACE ####

    def __init__(self, filename: str) ->None:
        """
            Constructs a stream object by filename
        """
        self.file = File(filename)
        self.label = None
        self.stream_size = None
        pass

    def read_content(self) ->str:
        """
            Reads file content and returns as 'raw' content.
            Equivalent to returning txt data.
        """
        return self.file.read_contents()

    def read_clean_content(self) ->list:
        """
            Defined loosely via the following turing model:

            Input: a file previously defined
            Output: a list of prepared base data to work with,
            indexed with the first element as a string label.

            Step 1: Find filename suffix S
            Step 2: Associate S w/ a particular file reading algorithm A
            Step 3: Clean data using procedure A
            Step 4: Terminate if list has been cleaned
        """
        suffix = self.detect_suffix()
        if (suffix == None):
            return None

        ## TODO: Abstract away implementation
        if (suffix.lower() == 'csv'):
            # Clean Data
            file_lines = self.file.read_contents()
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

    #### GETTERS/SETTERS ####

    @property
    def file(self) ->File:
        return self.__file

    @file.getter
    def file(self) ->File:
        return self.__file
    
    @file.setter
    def file(self, new_filename: str) ->str:
        print(f"Error: file created using {new_filename} cannot be re-set.")
        return self.file

    @property
    def label(self) ->str:
        return self.__label

    @label.getter
    def label(self) ->str:
        return self.__label
    
    @label.setter
    def label(self, new_label: str) ->str:
        self.label = str(new_label)
        return self.label

    @property
    def stream_size(self) ->int:
        return self.__stream_size

    @stream_size.getter
    def stream_size(self) ->int:
        return self.__stream_size
    
    @stream_size.setter
    def stream_size(self, new_stream_size: int) ->int:
        print("Error: attribute stream size cannot be set")
        return self.stream_size

    #### PRIVATE ####

    #### METHODS ####
    def detect_suffix(self) ->str:
        """
            Returns the suffix of the filename as a string.
            As python strings are immutable, this forms an
            enumerator - equivalent for purposes of control.
        """
        path = self.file.absolute_path
        suffix_start_index = -1
        for i, char in enumerate(path):
            if (char == '.'):
                suffix_start_index = i
        
        if (suffix_start_index == -1):
            print(f"Error: Suffix of filename: {path} not found or is not compatible.")
            return None

        return path[suffix_start_index : len(path)]

    #### DATA ####

    __file: File
    __label: str
    __stream_size: int

    pass