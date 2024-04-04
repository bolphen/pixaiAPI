An *unofficial* API for Pixai.art for Python using request

Original authored by [shidktbw](https://github.com/shidktbw/pixaiAPI).

This is my fork with img2img capability.

The `repaint.py` accepts a png and some prompts, and then replaces the png with the generated image.
```bash
repaint.py image.png "some prompts"
```

There are three main options in `repaint.py` that you can change.
- `token`: the token is needed for authorization and operation of requests from your account. I provided one from a throwaway account for testing purpose. Please replace it with your own. To obtain the token
1. Open DevTools in your browser
2. Go to Storage -> Local Storage -> `api.pixai.art:token`
3. Copy `value`

- `model`: models on pixai.art have urls of the form `pixai.art/model/12345/67890`. You should use the second number which refers to the specific version of a model.

- `high_priority`: once you replaced the token with your own, you can set it to `True` for faster generation.

**Note** If you want to use this for the Avatar mod, make sure `repaint.py` is executable and provide its full path in the settings of Avatar. You can then launch AI-gen tasks by right-clicking on the avatar, and they will show up in-game automatically once the generation has finished.
