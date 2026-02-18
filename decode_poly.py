def decode_polyline(polyline_str):
    index, lat, lng = 0, 0, 0
    coordinates = []
    while index < len(polyline_str):
        b, shift, result = 0, 0, 0
        while True:
            b = ord(polyline_str[index]) - 63
            index += 1
            result |= (b & 0x1f) << shift
            shift += 5
            if b < 0x20: break
        dlat = ~(result >> 1) if (result & 1) else (result >> 1)
        lat += dlat
        shift, result = 0, 0
        while True:
            b = ord(polyline_str[index]) - 63
            index += 1
            result |= (b & 0x1f) << shift
            shift += 5
            if b < 0x20: break
        dlng = ~(result >> 1) if (result & 1) else (result >> 1)
        lng += dlng
        coordinates.append((lat / 100000.0, lng / 100000.0))
    return coordinates

poly = "yuu{F_rgLfAbBHDV@HKJPBBf@u@BEFBjA\\r@Eh@E^f@DEPWV\\xB_DXc@U[R[TZR[h@q@v@cAV_@HOFV|AxBp@bAbB|BXf@v@lAPPf@t@`AtAp@z@MRDHLSDFMNFJLQPVRZl@z@tAnBxAvBZd@Nb@RXV\\VTR`@z@dAv@jARf@r@bAJBbAxAW\\LPDDRW|@rATR\\d@x@lAxDtFNTORV`@NUDD?FLRZc@MQRUVYBCCBWXSTLP[b@MSOTINORkBhCJLQTKMa@j@{BzCHJQVIMa@h@yBvCQTAGIKIJU]JKIMQGS[[e@uB_DW`@KQJUFM]e@q@aAiAaBkBpC@Bm@rAODCGs@fAaB~BNTQXuDoFiCyDe@u@CBEEBEW]gA_BcAyASZSU}@rAYZg@r@U]KRCDT\\QVm@|@Yb@KVm@z@ACYc@ORCBJLNVyAtBo@t@c@n@]f@GKGWQ]a@u@YYKJNZ}@z@IFACEF@D{A|AACEDEDeBdBKLEGIL@B}@~@{@t@GLcBbBoAlAoAlAEKKJFJONk@j@u@r@sBrBa@`@CEGFBDQTSPQJ[\\]XU\\_@Xo@p@MQCB[f@KQIJ[`@STDNEFEMU\\]d@w@fAa@l@e@l@aBxBgBlCw@`A]d@BDKLq@gAMXCHE@KDCGILGFI?UA[@KBKLGLEZW^CSBGJUA_@EQQm@AF?NDNG?F?EO?O@GPl@DP@NCVKTBRV_@Li@JMJCp@?H?FGHMBFJEDABILYp@fAJMCEhA}AzAuBnBmCz@iAdA}Al@{@LQDLFIGMRUZa@HKVb@V\\rBjD@HHJVt@dA~DjAxEZfACB@BFJXbAv@nCPLJf@P^ED@DDCDFFIl@v@X`@TVHARCDAT?FIbAhA`@d@FI`@g@Zc@LM`@ORULKz@s@zEsD|AkADLn@nBZz@"
coords = decode_polyline(poly)
for c in coords[:5]: print(c)
print("...")
for c in coords[-5:]: print(c)

min_lat = min(c[0] for c in coords)
max_lat = max(c[0] for c in coords)
min_lng = min(c[1] for c in coords)
max_lng = max(c[1] for c in coords)
print(f"Bounds: ({min_lat}, {min_lng}) - ({max_lat}, {max_lng})")
