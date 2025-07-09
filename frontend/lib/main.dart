import 'package:flutter/material.dart';
import 'screens/login_page.dart';
import 'screens/home_page.dart';
import 'screens/map_page.dart';
import 'screens/alert_history_page.dart';
import 'screens/alert_details_page.dart';

void main() {
  runApp(const GunshotApp());
}

class GunshotApp extends StatelessWidget {
  const GunshotApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Gunshot Detection',
      theme: ThemeData(primarySwatch: Colors.red),
      initialRoute: '/login',
      routes: {
        '/login': (_) => const LoginPage(),
        '/home': (_) => const HomePage(),
        '/map': (_) => const MapPage(),
        '/history': (_) => const AlertHistoryPage(),
      },
    );
  }
}
