img64
=====

A minimal Python server that can receive requests for external image
links and encode them in the `base64` format.

This project was made in order to get around [the `canvas.toDataURL`
security exception](http://stackoverflow.com/questions/2390232/why-does-canvas-todataurl-throw-a-security-exception).

As long as the requested image's `Content-Length` header is a reasonable
size, the image will be encoded and the response will be a `JSON` object
containing the data.
