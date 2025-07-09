import 'package:flutter/material.dart';

class MapPage extends StatelessWidget {
  const MapPage({super.key});

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      appBar: AppBar(title: Text('Map')),
      body: Center(
        child: Text('Map goes here'), // Integrate Google Map here
      ),
    );
  }
}
