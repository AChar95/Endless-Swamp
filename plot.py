import json

def plot():
    try:
        plotFile = open('./data_files/plot.json', 'r')
        plotExtractor = json.load(plotFile)
        if len(plotExtractor) > 0:
            return plotExtractor
        else:
            print("File is not formated properly")
    except IOError:
        print("Plot file cannot be found")
    except ValueError:
        print("Json plot file could not be read properly")
        
        
if __name__ == "__main__":
    plot()