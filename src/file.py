from pathlib import Path
from os import path

class File :
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

    def get_relative_path(self) ->str:
        return self.__relative_path

    def get_abs_path(self) ->str:
        """
            Return absolute path
        """
        if (self.__absolute_path == None) :
            absolute_path = self.__abs_from_relative()
            assert(absolute_path != None)
            return absolute_path
        else :
            return self.__absolute_path

    def get_contents(self) ->str:
        """
            returns the contents of the file
        """
        assert(self.__relative_path != None)

        abs_path = self.get_abs_path()
        assert(abs_path != None)

        path = open(abs_path, 'r', encoding='utf-8')
        content = path.read().splitlines()

        return content

    def __abs_from_relative(self) ->str:
        """
            Create an absolute file path from
            relative path if not already defined
        """
        file_path = path.abspath(self.__relative_path)
        assert(file_path != None)

        if (path.isabs(file_path)) :
            self.__absolute_path = file_path
            return self.__absolute_path
        else :
            return None

    #### PRIVATE ####

    __absolute_path:str
    __relative_path:str

    pass