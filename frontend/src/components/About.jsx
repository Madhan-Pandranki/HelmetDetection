const About = () => {
  return (
    <div className="max-w-4xl mx-auto py-8 px-4">
      <h1 className="text-3xl font-bold mb-4">
        About Our Helmet Detection System
      </h1>
      <p className="mb-4">Welcome to our Helmet Detection System!</p>
      <p className="mb-4">
        Our system is designed to enhance safety in various environments by
        detecting whether individuals are wearing helmets.
      </p>
      <h2 className="text-xl font-semibold mb-2">Features:</h2>
      <ul className="list-disc pl-6 mb-4">
        <li>Real-time detection of helmets using computer vision algorithms</li>
        <li>Integration with surveillance cameras for continuous monitoring</li>
        <li>Customizable alerts and notifications for non-compliance</li>
        <li>Dashboard for monitoring and analyzing helmet compliance trends</li>
      </ul>
      <h2 className="text-xl font-semibold mb-2">Our Team:</h2>
      <p className="mb-4">
        Our team consists of experienced engineers and data scientists
        passionate about using technology to improve safety.
      </p>
      <ul className="list-disc pl-6 mb-4">
        <li>Name 1</li>
        <li>Name 1</li>
        <li>Name 1</li>
        <li>Name 1</li>
      </ul>
      <h2 className="text-xl font-semibold mb-2">Technical Details:</h2>
      <p className="mb-4">
        Our system is built using the following technologies:
      </p>
      <ul className="list-disc pl-6 mb-4">
        <li>React for the frontend user interface</li>
        <li>Django for the backend server</li>
        <li>PyTorch for the computer vision algorithms</li>
        <li>WebRTC for streaming video from surveillance cameras</li>
      </ul>
    </div>
  );
};

export default About;
