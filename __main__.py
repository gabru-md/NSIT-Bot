import sys

if __name__ == "__main__":
    import nsitbot
    
    if '-version' in sys.argv:
        print nsitbot.__version__