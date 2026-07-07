import keyword

def main():
    print("Keywords available in Python:")
    for kw in keyword.kwlist:
        print(f"- {kw}")

if __name__ == "__main__":
    main()
