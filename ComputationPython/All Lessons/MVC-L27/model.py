import re
class Model:

    def __init__(self, email):
        self.email = email

# use property decorator to use getters & setters
# define email an attribute of Model
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        """
        Validate the email
        :param value:
        :return:
        """
        # create regular expression to match email input
        pattern = r'\b[A-Za-z0-9._%+-]+@floridapoly.edu\b'
        # \b word boundary indicates pattern is bounded by non-word character

        # check for match between reg_ex and input
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address (must be floridapoly domain): {value}')

    def save(self):

        """
        Save the email into a file
        :return:
        """
        with open('email_input.txt', 'a') as f:
            f.write(self.email + '\n')
