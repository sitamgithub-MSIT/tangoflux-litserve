# TangoFlux LitServe

[![Open In Studio](https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg)](https://lightning.ai/sitammeur/studios/deploy-tangoflux-audio-generation-model)

TangoFlux, a novel audio generation model, uses Diffusion Transformers conditioned on text and duration to produce high-quality audio. To achieve superior results, it employs a three-stage training process, including preference optimization using synthetic data. This project shows how to create a self-hosted, private API that deploys TangoFlux [text-to-audio model](https://huggingface.co/declare-lab/TangoFlux) with LitServe, an easy-to-use, flexible serving engine for AI models built on FastAPI.

## Project Structure

The project is structured as follows:

- `server.py`: The file containing the main code for the web server.
- `client.py`: The file containing the code for client-side requests.
- `LICENSE`: The license file for the project.
- `README.md`: The README file that contains information about the project.
- `assets`: The folder containing screenshots for working on the application.
- `.gitignore`: The file containing the list of files and directories to be ignored by Git.

## Tech Stack

- Python (for the programming language)
- PyTorch (for the deep learning framework)
- Hugging Face Transformers Library (for the model)
- LitServe (for the serving engine)

## Getting Started

To get started with this project, follow the steps below:

1. Run the server: `python server.py`
2. Upon running the server successfully, you will see uvicorn running on port 8000.
3. Open a new terminal window.
4. Run the client: `python client.py`

Now, you can see the model's output based on the input request. The model will generate an audio file based on the input prompt and duration.

## Usage

The project can be used to serve the TangoFlux text-to-audio model using LitServe. It allows you to input a text prompt and duration to generate an audio file, suggesting potential use cases in the audio generation domain, such as generating sound for videos, audiobooks, entertainment, and more.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you want to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the [Apache-2.0 License](LICENSE).

## Contact

If you have any questions or suggestions about the project, please contact me on my GitHub profile.

Happy coding! 🚀
