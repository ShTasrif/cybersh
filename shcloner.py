# Encrypted By PyEncryptor
# A Product Of ToxicNoob
# https://github.com/Toxic-Noob

import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode('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'))))