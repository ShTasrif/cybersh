# Encrypted By PyEncryptor
# A Product Of ToxicNoob
# https://github.com/Toxic-Noob

import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))