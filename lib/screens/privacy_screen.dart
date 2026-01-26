import 'package:flutter/material.dart';
import 'package:sehir_kesif/theme/wanderlust_colors.dart';

class PrivacyScreen extends StatelessWidget {
  const PrivacyScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: WanderlustColors.bgDark,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: const BackButton(color: Colors.white),
        title: const Text("Privacy & Terms", style: TextStyle(color: Colors.white)),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: const [
            Text(
              "Privacy Policy",
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.white),
            ),
            SizedBox(height: 16),
            Text(
              "Last updated: January 2026\n\n"
              "1. Introduction\n"
              "Welcome to My Way ('we', 'our', or 'us'). We are committed to protecting your personal information and your right to privacy.\n\n"
              "2. Information We Collect\n"
              "We collect personal information that you voluntarily provide to us when you use the accolades features.\n"
              "- Location Data: We use your location to provide route suggestions and navigation features.\n"
              "- Usage Data: We collect anonymous usage data to improve app performance.\n\n"
              "3. How We Use Your Information\n"
              "We use the information we collect or receive:\n"
              "- To facilitate account creation and logon process.\n"
              "- To send you marketing and promotional communications.\n"
              "- To deliver services to the user.\n\n"
              "4. Sharing Your Information\n"
              "We only share information with your consent, to comply with laws, to provide you with services, to protect your rights, or to fulfill business obligations.\n\n"
              "5. Contact Us\n"
              "If you have questions or comments about this policy, you may utilize the feedback form in the application.",
              style: TextStyle(fontSize: 14, color: Colors.white70, height: 1.5),
            ),
            SizedBox(height: 32),
            Divider(color: Colors.grey),
            SizedBox(height: 32),
            Text(
              "Terms of Use (EULA)",
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.white),
            ),
            SizedBox(height: 16),
            Text(
              "1. Agreement to Terms\n"
              "By using our application, you agree to be bound by these Terms of Use. If you do not agree, please do not use the application.\n\n"
              "2. Intellectual Property Rights\n"
              "Unless otherwise indicated, the Application is our proprietary property and all source code, databases, functionality, software, website designs, audio, video, text, photographs, and graphics on the Application are owned or controlled by us.\n\n"
              "3. User Representations\n"
              "By using the Application, you represent and warrant that: (1) all registration information you submit will be true, accurate, current, and complete; (2) you will maintain the accuracy of such information.\n\n"
              "4. Apple Standard EULA\n"
              "This application relies on the Standard Apple Terms of Use (EULA). https://www.apple.com/legal/internet-services/itunes/dev/stdeula/",
              style: TextStyle(fontSize: 14, color: Colors.white70, height: 1.5),
            ),
            SizedBox(height: 40),
          ],
        ),
      ),
    );
  }
}
