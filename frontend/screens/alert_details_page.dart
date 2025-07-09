import 'package:flutter/material.dart';

class AlertDetailsPage extends StatelessWidget {
  final String alertText;
  const AlertDetailsPage({super.key, required this.alertText});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Alert Details')),
      body: Padding(padding: const EdgeInsets.all(16), child: Text(alertText)),
    );
  }
}
