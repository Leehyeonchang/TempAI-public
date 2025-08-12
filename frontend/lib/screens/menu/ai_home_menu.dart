// D:\Web_AI_Temp\frontend\lib\screens\menu\ai_home_menu.dart
import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:frontend/screens/menu/anomaly_screen.dart';

class AIHomeMenu extends StatelessWidget {
  const AIHomeMenu({super.key});

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 4,
      child: Scaffold(
        extendBodyBehindAppBar: true,
        backgroundColor: const Color(0xFFF3F4F6),
        appBar: PreferredSize(
          preferredSize: const Size.fromHeight(100),
          child: ClipRRect(
            child: BackdropFilter(
              filter: ImageFilter.blur(sigmaX: 12, sigmaY: 12),
              child: AppBar(
                backgroundColor: Colors.white.withOpacity(0.85),
                elevation: 6,
                shape: const RoundedRectangleBorder(
                  borderRadius:
                      BorderRadius.vertical(bottom: Radius.circular(16)),
                ),
                title: const Text(
                  '٩(๑•̀ㅂ•́)و AI Monitoring System',
                  style: TextStyle(
                    color: Color(0xFF1F2937),
                    fontWeight: FontWeight.bold,
                    fontSize: 20,
                    letterSpacing: 0.8,
                  ),
                ),
                centerTitle: true,
                bottom: const TabBar(
                  isScrollable: false,
                  indicator: UnderlineTabIndicator(
                    borderSide:
                        BorderSide(width: 4.0, color: Color(0xFF7C3AED)),
                    insets: EdgeInsets.symmetric(horizontal: 16),
                  ),
                  labelColor: Color(0xFF7C3AED),
                  unselectedLabelColor: Colors.grey,
                  labelStyle: TextStyle(fontWeight: FontWeight.bold),
                  tabs: [
                    Tab(
                        icon: Icon(Icons.warning_amber_rounded),
                        text: "AI 이상 감지"),
                    Tab(icon: Icon(Icons.trending_up), text: "실시간 추이"),
                    Tab(icon: Icon(Icons.insights), text: "히스토그램"),
                    Tab(icon: Icon(Icons.settings), text: "설정"),
                  ],
                ),
              ),
            ),
          ),
        ),
        body: const TabBarView(
          children: [
            AnomalyScreen(), // ⬅️ 순서 변경
            _PlaceholderPage("📈 실시간 추이 페이지", Colors.indigo),
            _PlaceholderPage("📊 히스토그램 페이지", Colors.deepOrange),
            _PlaceholderPage("⚙️ 설정 페이지", Colors.teal),
          ],
        ),
      ),
    );
  }
}

class _PlaceholderPage extends StatelessWidget {
  final String text;
  final Color color;

  const _PlaceholderPage(this.text, this.color, {super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.center,
      child: Card(
        elevation: 8,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        color: color.withOpacity(0.1),
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 40),
          child: Text(
            text,
            style: TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.bold,
              color: color,
              letterSpacing: 1.1,
            ),
          ),
        ),
      ),
    );
  }
}
