import sys
from google import genai

from dotenv import load_dotenv
load_dotenv()

def ramble():
    if len(sys.argv) < 2:
        print("example usage, $ ramble \"what is the answer to the life, the universe, and everything?\"")
    
    (_, prompt) = sys.argv
    with open('tension', 'r') as f:
        system_instruction = f.read()
    client = genai.Client()

    try:
        response = client.models.generate_content_stream(
            model='gemini-2.5-flash',
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.4,
            )
        )

        for chunk in response:
            sys.stdout.write(chunk.text)
            sys.stdout.flush()

        print()
    except Exception as e:
        print(f"\nerror {e}", file=sys.stderr)

if __name__ == "__main__":
    ramble()
