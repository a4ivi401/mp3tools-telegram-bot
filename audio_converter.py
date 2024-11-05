from pydub import AudioSegment 
import os

# Укажите путь к FFmpeg (замените на ваш путь)
ffmpeg_path = "C:\\ffmpeg\\bin"  # для Windows
# ffmpeg_path = "/usr/local/bin"  # для macOS/Linux

os.environ["PATH"] += os.pathsep + ffmpeg_path
AudioSegment.converter = os.path.join(ffmpeg_path, "ffmpeg.exe")  # для Windows
# AudioSegment.converter = os.path.join(ffmpeg_path, "ffmpeg")  # для macOS/Linux

def converter_audio(input_file, output_format):
  audio = AudioSegment.from_file(input_file)
  output_file = f"output.{output_format}"
  audio.export(output_format, format=output_format)
  return output_file