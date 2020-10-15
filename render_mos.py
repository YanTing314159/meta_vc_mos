#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    html = template.render(
        page_title="MOS 實驗表單 0",
        form_url="https://script.google.com/macros/s/AKfycbypuz_7Zq2jqKaZ3Qk19wWOt0nUV05DL5f38semhmJdGHp68A0/exec",
        form_id=0,
        questions=[
            {
                "title": "問題 1",
                "audio_path": "wavs/test1.wav",
                "name": "q1"
            },
            {
                "title": "問題 2",
                "audio_path": "wavs/test2.wav",
                "name": "q2"
            },
            {
                "title": "問題 3",
                "audio_path": "wavs/test1.wav",
                "name": "q3"
            },
            {
                "title": "問題 4",
                "audio_path": "wavs/test1.wav",
                "name": "q4"
            },
            {
                "title": "問題 5",
                "audio_path": "wavs/test1.wav",
                "name": "q5"
            },
            {
                "title": "問題 6",
                "audio_path": "wavs/test1.wav",
                "name": "q6"
            },
            {
                "title": "問題 7",
                "audio_path": "wavs/test1.wav",
                "name": "q7"
            },
            {
                "title": "問題 8",
                "audio_path": "wavs/test1.wav",
                "name": "q8"
            },
            {
                "title": "問題 9",
                "audio_path": "wavs/test1.wav",
                "name": "q9"
            },
            {
                "title": "問題 1",
                "audio_path": "wavs/test1.wav",
                "name": "q1"
            },
            {
                "title": "問題 10",
                "audio_path": "wavs/test1.wav",
                "name": "q10"
            },
            {
                "title": "問題 11",
                "audio_path": "wavs/test1.wav",
                "name": "q11"
            },
            {
                "title": "問題 12",
                "audio_path": "wavs/test1.wav",
                "name": "q12"
            },
            {
                "title": "問題 13",
                "audio_path": "wavs/test1.wav",
                "name": "q13"
            },
            {
                "title": "問題 14",
                "audio_path": "wavs/test1.wav",
                "name": "q14"
            },
            {
                "title": "問題 15",
                "audio_path": "wavs/test1.wav",
                "name": "q15"
            },
            {
                "title": "問題 16",
                "audio_path": "wavs/test1.wav",
                "name": "q16"
            },
            {
                "title": "問題 17",
                "audio_path": "wavs/test1.wav",
                "name": "q17"
            },
            {
                "title": "問題 18",
                "audio_path": "wavs/test1.wav",
                "name": "q18"
            },
            {
                "title": "問題 19",
                "audio_path": "wavs/test1.wav",
                "name": "q19"
            },
            {
                "title": "問題 20",
                "audio_path": "wavs/test1.wav",
                "name": "q20"
            },
        ]
    )
    print(html)


if __name__ == "__main__":
    main()
