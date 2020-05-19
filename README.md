# A Simple Amazon Transcribe data formatter
This program takes JSON data from Amazon Transcribe and formats it into a conversational format.

Example：
```text
spk_0: Hello
spk_1: Hi
spk_0: Nice to meet you!
spk_3: I'm glad to see you!
```
## usage
```bash
python format_asroutput.py -i PATH/TO/asrOutput.json -o PATH/TO/result.txt
```

## Arguments
### `-i/--input`
Required. Specify the input file.

### `-o/--output`
Option. Specifies the name of the output file, including the path.

If it is not specified, the output will be named as `result.txt` in the current directory.