import sys
from analyzer.parser import analyze_sentence

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py 'Your sentence here'")
        return
    
    sentence = sys.argv[1]
    result = analyze_sentence(sentence)
    print("Grammar analysis result:")
    for word, tag in result:
        print(f"{word} -> {tag}")

if __name__ == "__main__":
    main()
