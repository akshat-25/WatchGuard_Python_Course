class MyCustomError(TypeError):
    """
    Exception raised with code
    """
    def __init__(self,message,code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code
    

err =  MyCustomError("An Error Occured...",500) 
print(err.__doc__)