from pydub import AudioSegment 

def converter_audio(input_file, output_format):
  audio = AudioSegment.from_file(input_file)
  output_file = f"output.{output_format}"
  audio.export(output_format, format=output_format)
  return output_file