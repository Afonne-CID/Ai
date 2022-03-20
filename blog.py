#!/usr/bin/env python3
import os
import openai
import config


openai.api_key = config.OPENAI_API_KEY

def generateBlogSections(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the blog title in to high level blog sections: {} \n\n- Introduction: ".format(prompt1),
      temperature=0.6,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']


def blogSectionExpander(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the blog section in to a detailed professional , witty and clever explanation.\n\n {}".format(prompt1),
      temperature=0.7,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']

def blogWriter():
    """Loops through a .txt file and supplies input to `blogSectionExpander`
    """
    try:
        with open("./file.txt", "r") as f:
            lines = f.readlines()
            try:
                for line in lines:
                    print("Expanding {}...".format(line))
                    output = blogSectionExpander(line)
                    with open("./line.txt", 'a') as f:
                        f.write("\n\n\n" + line + "\n")
                        f.write(output)
                        print("done")
            except Exception as e:
                print(e)

    except:
        return "File doesn't exist"

if __name__ == "__main__":
    blogWriter()

