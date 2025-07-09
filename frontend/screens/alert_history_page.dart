import 'package:flutter/material.dart';

class AlertHistoryPage extends StatelessWidget {
  const AlertHistoryPage({super.key});

  @override
  Widget build(BuildContext context) {
    final alerts = [
      'Gunshot at Elm Street - 12:01 PM',
      'Siren detected near Market Road - 9:44 AM',
    ];

    return Scaffold(
      appBar: AppBar(title: const Text('Alert History')),
      body: ListView.builder(
        itemCount: alerts.length,
        itemBuilder: (_, index) => ListTile(title: Text(alerts[index])),
      ),
    );
  }
}
