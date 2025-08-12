import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = "http://127.0.0.1:8000"; // 백엔드 URL

  // 로그인 API
  static Future<Map<String, dynamic>> login(
    String userId,
    String password,
  ) async {
    final url = Uri.parse("$baseUrl/auth/login");
    final response = await http.post(
      url,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"user_id": userId, "password": password}),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception(jsonDecode(response.body)['detail'] ?? "로그인 실패");
    }
  }

  // 예측 API
  static Future<Map<String, dynamic>> getPrediction(
    String plantId,
    String resId,
    String tagName,
    double value,
  ) async {
    final url = Uri.parse(
      "$baseUrl/predict/?plant_id=$plantId&res_id=$resId&tag_name=$tagName&value=$value",
    );
    final response = await http.get(url);

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception("예측 API 호출 실패");
    }
  }
}
