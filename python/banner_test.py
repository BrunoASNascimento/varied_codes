import pyfiglet

string_value = 'Teste !!!'

print(pyfiglet.figlet_format(string_value))

custom_fig = pyfiglet.Figlet(font='graffiti')
print(custom_fig.renderText(string_value))
