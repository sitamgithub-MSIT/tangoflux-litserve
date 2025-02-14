import io
import torch
import torchaudio
import soundfile as sf
import litserve as ls
from tangoflux import TangoFluxInference
from fastapi.responses import Response


class TangoFluxAPI(ls.LitAPI):
    """
    TangoFluxAPI is a subclass of ls.LitAPI that provides an interface to the TangoFlux model for text-to-audio task.

    Methods:
        - setup(device): Called once at startup for the task-specific setup.
        - decode_request(request): Convert the request payload to model input.
        - predict(inputs): Uses the model to generate audio from the input prompt.
        - encode_response(output): Convert the model output to a response payload.
    """

    def setup(self, device):
        """
        Set up the model inference for text-to-audio task.
        """
        self.device = device
        self.model = TangoFluxInference(
            name="declare-lab/TangoFlux", device=self.device
        )

    def decode_request(self, request):
        """
        Convert the request payload to model input.
        """
        # Extract the inputs from request payload
        prompt = request.get("prompt")
        duration = request.get("duration", 10)

        # Return the inputs
        return prompt, duration

    def predict(self, inputs):
        """
        Run inference and generate audio file using the TangoFlux model.
        """
        # Get the inputs
        prompt, duration = inputs

        # Generate audio
        audio = self.model.generate(prompt, steps=50, duration=duration)

        # Ensure audio is in the correct format (2D Tensor: [channels, samples])
        if len(audio.shape) == 1:
            audio_tensor = audio.unsqueeze(0)
        elif len(audio.shape) == 2:
            audio_tensor = audio
        else:
            raise ValueError(f"Unexpected audio tensor shape: {audio.shape}")

        # Convert tensor to NumPy array
        final_audio = audio_tensor.cpu().numpy()

        # Save the final audio to a buffer
        audio_buffer = io.BytesIO()
        sf.write(audio_buffer, final_audio.T, 44100, format="WAV")
        audio_buffer.seek(0)
        audio_data = audio_buffer.getvalue()
        audio_buffer.close()

        # Return the audio data
        return audio_data

    def encode_response(self, output):
        """
        Convert the model output to a response payload.
        """
        # Package the generated audio data into a response
        return Response(content=output, media_type="audio/wav")


if __name__ == "__main__":
    # Create an instance of the TangoFluxAPI class and run the server
    api = TangoFluxAPI()
    server = ls.LitServer(api, track_requests=True)
    server.run(port=8000)
