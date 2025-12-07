from PIL import Image
from huggingface_hub import InferenceClient
from config import API_key

def generate_image_from_text(prompt: str) ->  Image.Image:
    try:
        client = InferenceClient(api_key=API_key)

        image = client.text_to_image(
            prompt = prompt,
            model = "black-forest-labs/FLUX.1-schnell"
        )
        return image
    except Exception as e:
        raise Exception(f"Image generation failed: {e}")
def main():
    """"   Main loop for user interaction. Continuously prompts the user for a text description,
    generates an image via the API, displays it, and offers an option to save the image."""

    print("Welcome to the Text-to-Image Generator!")
    print("Type 'exit' to quit the program.\n")

    while True:
        prompt = input("Enter a text description for the image: ").strip()
        if prompt.lower() == 'exit':
            print("Goodbye!")
            break
        print("Generating image....")
        try:
            image = generate_image_from_text(prompt)
            image.show()

            save_option = input("Do you want to save the image? (yes/no): ").strip().lower()
            if save_option == 'yes':
                file_name = input("Enter the filename to save the image (without extension): ").strip().lower()
                file_name = "".join(c for c in file_name if c.isalnum() or c in ('_' ,'-')).rstrip()
                image.save(f"{file_name}.png")
                print(f"Image saved as {file_name}.png\n")
        except Exception as e:
            print(f"Ann error occurred: {e}\n")
        print("-" * 80 + "\n")
if __name__ == "__main__":
    main()