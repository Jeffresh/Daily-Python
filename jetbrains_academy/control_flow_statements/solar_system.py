# Create a file planets.txt and write the names of the Solar system planets there,
# each on a new line. In total, the file should contain 8 lines with the following planets:
# Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.
# When opening the file, specify encoding='utf-8'.

if __name__ == '__main__':
    planets = ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n', 'Saturn\n', 'Uranus\n', 'Neptune']

    file = open('planets.txt', mode='w', encoding='utf-8')
    file.writelines(planets)
    file.close()
