import ndef
record1 = nfc.ndef.Record("urn:nfc:wkt:T", "id1", "\x02enHello World!")
record2 = nfc.ndef.Record("urn:nfc:wkt:T", "id2", "\x02deHallo Welt!")
encoder = ndef.message_encoder()
encoder.send(None)
encoder.send(record1)
encoder.send(record2)
encoder.send(None)
message = [record1, record2]
list((ndef.message_encoder(message, open('ndef.dat', 'w+b'))))
