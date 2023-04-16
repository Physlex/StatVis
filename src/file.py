from os import path

class File :
    """
        Abstraction for path representation of a file.
        Primarily abstracts collection of arbitrary text data
            from some relative file location.
    """
    #### PUBLIC ####

    def __init__(self, file_path) -> None:
        """
            Constructs a path object
        """

        if (path.isfile(file_path) == False) :
            print(f"Error: {file_path} is invalid")
        else :
            self.__relative_path = file_path
        
        if (path.isabs(file_path) == True) :
            self.__absolute_path = file_path
        else :
            self.__absolute_path = None
        pass

    #### INTERFACE ####

    def read_contents(self) ->str:
        """
            reads and returns the raw contents of the file
        """
        assert(self.__relative_path != None)

        abs_path = self.absolute_path
        assert(abs_path != None)

        path = open(abs_path, 'r', encoding='utf-8')
        content = path.read().splitlines()

        return content

    #### GETTERS / SETTERS ####

    @property
    def relative_path(self) ->str:
        return self.__relative_path

    @relative_path.getter
    def relative_path(self) ->str:
        return self.__relative_path

    @property
    def absolute_path(self) ->str:
        return self.__absolute_path

    @absolute_path.getter
    def absolute_path(self) ->str:
        """
            Return absolute path to file.
        """
        if (self.__absolute_path == None) :
            absolute_path = self.__abs_from_relative()
            assert(absolute_path != None)
            return absolute_path
        else :
            return self.__absolute_path

    #### PRIVATE_METHODS ####

    def __abs_from_relative(self) ->str:
        """
            Create an absolute file path from relative
        """
        file_path = path.abspath(self.__relative_path)
        assert(file_path != None)

        if (path.isabs(file_path)) :
            self.__absolute_path = file_path
            return self.__absolute_path
        else :
            return None

    #### ATTRIBUTES ####

    __absolute_path:str
    __relative_path:str
