import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  final List<Map<String, dynamic>> mockAlerts;

  const HomePage({super.key, required this.mockAlerts}); // Require mockAlerts

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Gunshot Alerts")),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Column(
                  children: [
                    IconButton(
                      icon: const Icon(
                        Icons.map,
                        size: 40,
                        color: Colors.blueGrey,
                      ),
                      onPressed: () {
                        Navigator.pushNamed(
                          context,
                          '/map',
                        ); // Navigate to Map Page
                      },
                    ),
                    const Text(
                      "Maps",
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
                Column(
                  children: [
                    IconButton(
                      icon: const Icon(
                        Icons.history,
                        size: 40,
                        color: Colors.blueGrey,
                      ),
                      onPressed: () {
                        Navigator.pushNamed(
                          context,
                          '/history',
                        ); // Navigate to Alert History
                      },
                    ),
                    const Text(
                      "Alert History",
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
          Expanded(
            child:
                mockAlerts.isEmpty
                    ? const Center(
                      child: Text(
                        "No alerts available",
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    )
                    : ListView.separated(
                      itemCount: mockAlerts.length,
                      separatorBuilder: (context, index) => const Divider(),
                      itemBuilder: (context, index) {
                        final alert = mockAlerts[index];
                        return Card(
                          margin: const EdgeInsets.symmetric(
                            horizontal: 16,
                            vertical: 8,
                          ),
                          child: ListTile(
                            contentPadding: const EdgeInsets.all(
                              12,
                            ), // Add padding
                            title: Text(
                              alert["description"],
                              style: const TextStyle(
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                            subtitle: Text(
                              "Time: ${alert["time"]}, Date: ${alert["date"]}",
                            ),
                            leading: const Icon(
                              Icons.warning,
                              color: Colors.red,
                              size: 32,
                            ),
                            trailing: const Icon(
                              Icons.arrow_forward_ios,
                              size: 18,
                              color: Colors.grey,
                            ),
                            onTap: () {
                              Navigator.pushNamed(
                                context,
                                '/alertDetails',
                                arguments: alert, // Pass alert details
                              );
                            },
                          ),
                        );
                      },
                    ),
          ),
        ],
      ),
    );
  }
}
