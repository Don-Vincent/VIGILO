import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;

class ApiService {
  static Future<String> predictGunshot(File audioFile) async {
    final uri = Uri.parse('http://127.0.0.1:5000/predict');
    var request = http.MultipartRequest('POST', uri);
    request.files.add(
      await http.MultipartFile.fromPath('audio', audioFile.path),
    );
    var response = await request.send();

    final respStr = await response.stream.bytesToString();
    final json = jsonDecode(respStr);
    return json['prediction'].toString();
  }
}
