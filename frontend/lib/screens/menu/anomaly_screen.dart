// D:\Web_AI_Temp\frontend\lib\screens\menu\anomaly_screen.dart
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:fl_chart/fl_chart.dart';

class AnomalyScreen extends StatefulWidget {
  const AnomalyScreen({super.key});

  @override
  State<AnomalyScreen> createState() => _AnomalyScreenState();
}

class _AnomalyScreenState extends State<AnomalyScreen> {
  bool _loading = false;
  double? _predictedValue;
  String? _isAnomaly;

  Future<void> _fetchPrediction() async {
    setState(() => _loading = true);

    try {
      final url = Uri.parse(
        "http://127.0.0.1:8000/predict?plant_id=01&res_id=59-066&tag_name=S3_TEMP",
      );

      final response = await http.get(url);

      if (response.statusCode == 200) {
        final data = jsonDecode(utf8.decode(response.bodyBytes));

        setState(() {
          _predictedValue = data["predicted_value"];
          _isAnomaly = data["is_anomaly"];
        });
      } else {
        setState(() {
          _predictedValue = null;
          _isAnomaly = "오류 발생";
        });
      }
    } catch (e) {
      setState(() {
        _predictedValue = null;
        _isAnomaly = "서버 연결 실패";
      });
    } finally {
      setState(() => _loading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar:
          AppBar(title: const Text("창현이의 AI 이상 감지 ‧⁺◟( ᵒ̴̶̷̥́ ·̫ ᵒ̴̶̷̣̥̀ ) ")),
      body: Center(
        child: _loading
            ? const CircularProgressIndicator()
            : Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  ElevatedButton(
                    onPressed: _fetchPrediction,
                    child: const Text("AI 예측 실행"),
                  ),
                  const SizedBox(height: 20),
                  if (_predictedValue != null) ...[
                    Text(
                      "예측값: $_predictedValue",
                      style: const TextStyle(fontSize: 18),
                    ),
                    Text(
                      "이상 여부: $_isAnomaly",
                      style: TextStyle(
                        fontSize: 18,
                        color: _isAnomaly == "Y" ? Colors.red : Colors.green,
                      ),
                    ),
                    const SizedBox(height: 30),
                    SizedBox(
                      height: 200,
                      child: BarChart(
                        BarChartData(
                          alignment: BarChartAlignment.center,
                          barGroups: [
                            BarChartGroupData(
                              x: 0,
                              barRods: [
                                BarChartRodData(
                                  toY: _predictedValue ?? 0,
                                  color: Colors.blue,
                                  width: 30,
                                ),
                              ],
                            ),
                          ],
                        ),
                      ),
                    ),
                  ],
                ],
              ),
      ),
    );
  }
}
