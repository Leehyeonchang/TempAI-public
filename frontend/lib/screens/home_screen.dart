import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // 로그인에서 전달된 데이터 받기
    final arguments = ModalRoute.of(context)?.settings.arguments;

    return Scaffold(
      appBar: AppBar(title: const Text('AILEE HOME'), centerTitle: true),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'go',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),

            const SizedBox(height: 16),

            // Text(
            //   '받은 데이터: ${arguments.toString()}',
            //   style: const TextStyle(fontSize: 16),
            // ),
            const SizedBox(height: 32),

            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/menu'); // ✅ AI 홈 메뉴로 이동
              },
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(
                  horizontal: 32,
                  vertical: 16,
                ),
              ),
              child: const Text('AI 메뉴로 이동', style: TextStyle(fontSize: 18)),
            ),
          ],
        ),
      ),
    );
  }
}
