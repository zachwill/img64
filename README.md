[img64](http://img64.com)
=========================

A minimal Python server that can receive requests for external image
links and encode them in the `base64` format. This project was made in
order to get around [the `canvas.toDataURL` security
exception](http://stackoverflow.com/questions/2390232/why-does-canvas-todataurl-throw-a-security-exception).

As long as the requested image's `Content-Length` header is a reasonable
size, the image will be encoded and the response will be a `JSON` object
containing the data.

**Bonus**: External text and HTML can be encoded, too -- although the
purpose remains `base64` encoding images.


Usage
-----

If you were using a JavaScript library like jQuery, you could get the
encoding of an external image like so...

```javascript
var image = "http://flask.pocoo.org/static/logo.png";

$.ajax({
  url: 'http://img64.com/?q=' + encodeURIComponent(image),
  dataType: 'jsonp'
}).then(function (data) {
  console.log(data)
})
```

For further instructions on usage, just [visit the site](http://img64.com).

[`http://img64.com`](http://img64.com)

To encode images by visiting the site, pass the URL a `q` argument pointing to the image
link.

[`http://img64.com/?q=https://si0.twimg.com/a/1321379639/phoenix/img/twitter_logo_right.png`](http://img64.com/?q=https://si0.twimg.com/a/1321379639/phoenix/img/twitter_logo_right.png)
