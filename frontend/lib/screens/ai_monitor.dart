import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:fl_chart/fl_chart.dart';

class AIMonitorScreen extends StatefulWidget {
  const AIMonitorScreen({Key? key}) : super(key: key);

  @override
  State<AIMonitorScreen> createState() => _AIMonitorScreenState();
}

class _AIMonitorScreenState extends State<AIMonitorScreen> {
  List<FlSpot> actualData = [];
  List<FlSpot> predictedData = [];
  bool isLoading = false;
  String statusMessage = "";

  int counter = 0; // X축 데이터 인덱스

  Future<void> fetchPrediction() async {
    setState(() => isLoading = true);

    try {
      // final url = Uri.parse("http://127.0.0.1:8000/predict?plant_id=01&res_id=EQP01&tag_name=OIL_TEMP_ACT&value=40.5");
      final url = Uri.parse(
          "http://127.0.0.1:8000/predict?plant_id=01&res_id=59-066&tag_name=S3_TEMP");
      final response = await http.get(url);

      if (response.statusCode == 200) {
        final data = jsonDecode(utf8.decode(response.bodyBytes));

        double actual = data["input_value"] ?? 0;
        double predicted = data["predicted_value"] ?? 0;
        bool isAnomaly = (data["is_anomaly"] == "Y");

        setState(() {
          actualData.add(FlSpot(counter.toDouble(), actual));
          predictedData.add(FlSpot(counter.toDouble(), predicted));
          counter++;

          statusMessage = isAnomaly ? "⚠ 이상 발생!" : "정상 상태";
        });
      } else {
        setState(() => statusMessage = "❌ 서버 오류");
      }
    } catch (e) {
      setState(() => statusMessage = "🔥 연결 실패: $e");
    } finally {
      setState(() => isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("⚠ AI 이상 감지")),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            ElevatedButton(
              onPressed: isLoading ? null : fetchPrediction,
              child: isLoading
                  ? const CircularProgressIndicator(color: Colors.white)
                  : const Text("예측 실행"),
            ),
            const SizedBox(height: 12),
            Text(
              statusMessage,
              style: TextStyle(
                fontSize: 18,
                color: statusMessage.contains("이상") ? Colors.red : Colors.green,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 20),
            Expanded(
              child: LineChart(
                LineChartData(
                  titlesData: FlTitlesData(
                    leftTitles: AxisTitles(
                      sideTitles:
                          SideTitles(showTitles: true, reservedSize: 40),
                    ),
                    bottomTitles: AxisTitles(
                      sideTitles: SideTitles(showTitles: true),
                    ),
                  ),
                  lineBarsData: [
                    LineChartBarData(
                      spots: actualData,
                      isCurved: true,
                      color: Colors.blue,
                      barWidth: 3,
                      dotData: FlDotData(show: true),
                    ),
                    LineChartBarData(
                      spots: predictedData,
                      isCurved: true,
                      color: Colors.red,
                      barWidth: 3,
                      dotData: FlDotData(show: true),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
